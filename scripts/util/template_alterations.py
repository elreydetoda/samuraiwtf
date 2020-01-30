#!/usr/bin/env python3
import json
from pprint import pprint

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

    variables_dict.update(sub_list)
    return json_obj

def builders_alterations(json_obj):
    # only selecting the vars section from the template
    builders_list = json_obj['builders']

    allowed_builders_list = [ 'virtualbox-iso', 'vmware-iso']

    for builder in builders_list:
        if builder['type'] not in allowed_builders_list:
            print(builder['type'])
            builders_list.remove(builder)

    # for builder in builders_list:
        # print(builder)
        # print(builder['type'])
    # print(builders_list)

if __name__ == "__main__":
    old_packer_file = bento_debian_path + '/debian-10.2-amd64.json'
    new_packer_file = 'samurai.json'

    # read in file
    with open(old_packer_file, 'r') as current_template:
        data = current_template.read()

    # replacing all instances of template dir with a user var
    #   of bento_debian_path, because that is the location it
    #   is expecting for relative file traversal
    data = data.replace('template_dir', 'user `bento_debian_dir`')

    # converting to json object
    obj = json.loads(data)

    updated_obj = var_alterations(obj)
    updated_obj = builders_alterations(updated_obj)
    # pprint(updated_obj)
