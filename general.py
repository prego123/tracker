import os

#Each website is a separate project (Folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project"+directory)
        os.makedirs(directory)

#Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue=os.path.join(project_name, 'queue.txt')
    crawled=os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


#add data onto an existing file

def append_to_filename(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

#delete the contents of a file
def delete_file_content(path):
    open(path, 'w').close()

#read a file and convert each line to set items
def file_to_set(file_name):
    results=set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

#iterate through a set, each item will be a new line in a file
def set_to_file(links, file_name):
    with open(file_name, 'w') as f:
        for l in sorted(links):
            f.write(l+"\n")
    

