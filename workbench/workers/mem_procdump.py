
''' Memory Image ProcDump worker. This worker utilizes the Rekall Memory Forensic Framework.
    See Google Github: http://github.com/google/rekall
    All credit for good stuff goes to them, all credit for bad stuff goes to us. :)
'''

from rekall_adapter.rekall_adapter import RekallAdapter
import zerorpc
import contextlib
import tempfile
import shutil
import glob, os
import hashlib
import pprint

class MemoryImageProcDump(object):
    ''' This worker dumps process pe files from memory image files. '''
    dependencies = ['sample']

    def __init__(self):
        ''' Initialization '''
        self.output = {}
        self.plugin_name = 'procdump'

        # Spin up workbench connection
        self.c = zerorpc.Client(timeout=300, heartbeat=60)
        self.c.connect("tcp://127.0.0.1:4242")        

    def execute(self, input_data):
        ''' Execute method '''

        # Grab the raw bytes of the sample
        raw_bytes = input_data['sample']['raw_bytes']

        # Spin up the rekall adapter
        adapter = RekallAdapter(raw_bytes)
        session = adapter.get_session()
        renderer = adapter.get_renderer()

        # Create a temporary directory
        with self.goto_temp_directory():

            # Here we can grab any plugin
            try:
                plugin = session.plugins.procdump()
            except KeyError:
                print 'Could not load the %s Rekall Plugin.. Failing with Error.' % self.plugin_name
                return {'Error': 'Could not load the %s Rekall Plugin' % self.plugin_name}

            # Render the plugin and grab all the dumped files
            renderer.render(plugin)

            # Scrape any extracted files
            print 'mem_procdump: Scraping dumped files...'
            self.output['dumped_files'] = []
            for output_file in glob.glob('*'):

                # Store the output into workbench, put md5s in the 'dumped_files' field
                output_name = os.path.basename(output_file)
                output_name = output_name.replace('executable.', '')
                with open(output_file, 'rb') as dumped_file:
                    raw_bytes = dumped_file.read()
                    md5 = self.c.store_sample(raw_bytes, output_name, 'exe')

                    # Remove some columns from meta data
                    meta = self.c.work_request('meta', md5)['meta']
                    del meta['customer']
                    del meta['encoding']
                    del meta['import_time']
                    del meta['mime_type']
                    self.output['dumped_files'].append(meta)

        # Organize the output a bit
        self.output['tables'] = ['dumped_files']
        return self.output

    @contextlib.contextmanager
    def goto_temp_directory(self):
        previousDir = os.getcwd()
        temp_dir = tempfile.mkdtemp()
        os.chdir(temp_dir)
        try:
            yield temp_dir
        finally:
            # Change back to original directory
            os.chdir(previousDir)
            # Remove the directory/files
            shutil.rmtree(temp_dir)

    def __del__(self):
        ''' Class Cleanup '''
        # Close zeroRPC client
        self.c.close()




# Unit test: Create the class, the proper input and run the execute() method for a test
import pytest
@pytest.mark.rekall
def test():
    ''' mem_procdump.py: Test '''

    # This worker test requires a local server running
    import zerorpc
    workbench = zerorpc.Client(timeout=300, heartbeat=60)
    workbench.connect("tcp://127.0.0.1:4242")

    # Store the sample
    data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data/memory_images/exemplar4.vmem')
    with open(data_path, 'rb') as mem_file:
        raw_bytes = mem_file.read()
        md5 = hashlib.md5(raw_bytes).hexdigest()
        if not workbench.has_sample(md5):
            md5 = workbench.store_sample(open(data_path, 'rb').read(), 'exemplar4.vmem', 'mem')

    # Execute the worker (unit test)
    worker = MemoryImageProcDump()
    output = worker.execute({'sample':{'raw_bytes':raw_bytes}})
    print '\n<<< Unit Test >>>'
    pprint.pprint(output)
    assert 'Error' not in output

    # Execute the worker (server test)
    output = workbench.work_request('mem_procdump', md5)
    print '\n<<< Server Test >>>'
    pprint.pprint(output)
    assert 'Error' not in output


if __name__ == "__main__":
    test()
