#!/usr/bin/env python3
from time import sleep
import json
from pprint import pprint

## global variables
scripts_path = './scripts'
build_script = scripts_path + '/build'
ansible_scripts = scripts_path + '/'
bento_path = build_script + '/bento'
bento_debian_path = bento_path + '/packer_templates/debian'
base_box_name = 'samuraiewtf-base_box'

# alterations to the variables section of the packer template
def var_alterations(json_obj):

    # only selecting the vars section from the template
    variables_dict = json_obj['variables']

    # list of items to remove from the template
    remove_list = [ 'version', 'http_proxy', 'https_proxy', 'no_proxy',
        'mirror', 'mirror_directory', 'iso_name', 'build_timestamp',
        'git_revision', 'guest_additions_url' ]

    # removing all items in list above
    for var in remove_list:
        del variables_dict[var]

    # either adding or updating values in template
    sub_list = {
        'headless': '',
        'iso_checksum': '',
        'iso_checksum_type': '',
        'build_directory': './builds',
        'bento_debian_dir': bento_debian_path,
        'box_basename': base_box_name,
        'http_directory': bento_debian_path + '/http'
    }

    # making alteration as defined above
    variables_dict.update(sub_list)

    # returning altered object
    return json_obj

# alterations to the builders section of the packer template
def builders_alterations(json_obj):
    # only selecting the vars section from the template
    builders_list = json_obj['builders']

    # currently supported builders
    allowed_builders_list = [ 'virtualbox-iso', 'vmware-iso']
    removal_builders_list = [ ]

    # removing unsupported builders
    for builder in builders_list:
        if builder['type'] not in allowed_builders_list:
            print(builder['type'])
            removal_builders_list.append(builder)

    for removed in removal_builders_list:
        builders_list.remove(removed)

    return builders_list

if __name__ == "__main__":
    # location of old debian template
    old_packer_file = bento_debian_path + '/debian-10.2-amd64.json'
    # location of file getting outputted
    new_packer_file = 'samurai.json'

    # read in old file
    with open(old_packer_file, 'r') as current_template:
        data = current_template.read()

    # replacing all instances of template dir with a user var
    #   of bento_debian_path, because that is the location it
    #   is expecting for relative file traversal
    data = data.replace('template_dir', 'user `bento_debian_dir`')

    # converting to json object
    obj = json.loads(data)

    # altering variable section of packer json template
    updated_obj = var_alterations(obj)

    # altering builders section of packer json template
    updated_obj = builders_alterations(updated_obj)
    # pprint(updated_obj)
