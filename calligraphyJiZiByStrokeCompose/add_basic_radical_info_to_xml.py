# coding: utf-8
import os
import cv2
import xml.etree.ElementTree as ET
import shutil


from utils.Functions import getSingleMaxBoundingBoxOfImage, prettyXml

char_775_path = '../../../Data/Calligraphy_database/Chars_775'
char_1000_path = '../../../Data/Calligraphy_database/Chars_1000'

char_merged = "../../../Data/Calligraphy_database/Chars_merged"

lp_processed = "../../../Data/Calligraphy_database/not_process_data_split/lp_processed"

xml_path = "../../../Data/Characters/jian_fan_merge_basic_radical_stroke.xml"

save_path = "../../../Data/Characters/jian_fan_merge_basic_radical_stroke_complement.xml"


def add_basic_radical_info_to_xml(root, path):
    if path == '':
        return
    # list all folders
    filenames = [f for f in os.listdir(path) if '.' not in f]
    print('file names len: ', len(filenames))

    for i in range(len(root)):
        element = root[i]
        tag = element.attrib["TAG"].strip()
        if len(tag) > 1:
            continue
        if not tag in filenames:
            continue

        if element.findall("BASIC_RADICALS"):
            continue

        # add basic radicals element
        basic_radicals_elem = ET.Element('BASIC_RADICALS')
        br_names = [f for f in os.listdir(os.path.join(path, tag, 'basic radicals')) if '.png' in f]

        for bn in br_names:

            b_radical_elem = ET.Element('BASIC_RADICAL')

            bn_folder = bn.replace('.png', '')
            stroke_names = [f for f in os.listdir(os.path.join(path, tag, 'basic radicals', bn_folder)) if '.png' in f]
            stroke_names = sorted(stroke_names)

            # id
            id = bn_folder.split('_')[-2]
            b_tag = bn_folder.split('_')[-1]
            # position
            r_img = cv2.imread(os.path.join(path, tag, 'basic radicals', bn), 0)
            r_post = getSingleMaxBoundingBoxOfImage(r_img)
            r_post = str([r_post[0], r_post[1], r_post[2], r_post[3]])

            b_radical_elem.set('ID', id)
            b_radical_elem.set('TAG', b_tag)
            b_radical_elem.set('POSITION', r_post)

            # strokes elemets
            strokes_elemt = ET.Element('STROKES')
            for sn in stroke_names:
                stroke_elemt = ET.Element('STROKE')

                s_id = sn.replace('.png', '').split('_')[-1]

                stroke_elemt.set('TAG', s_id)

                s_img = cv2.imread(os.path.join(path, tag, 'basic radicals', bn_folder, sn), 0)
                s_post = getSingleMaxBoundingBoxOfImage(s_img)
                stroke_elemt.text = str([s_post[0], s_post[1], s_post[2], s_post[3]])

                strokes_elemt.append(stroke_elemt)

            b_radical_elem.append(strokes_elemt)

            basic_radicals_elem.append(b_radical_elem)
        element.append(basic_radicals_elem)

    return root





def clean_png_in_radicals(path):

    chars = [f for f in os.listdir(path) if "." not in f]

    for ch in chars:
        radical_path = os.path.join(path, ch, "basic radicals")
        radical_img_names = [f for f in os.listdir(os.path.join(radical_path)) if ".png" in f]

        for ri in radical_img_names:
            if len(ri.split("_")) == 3:
                os.remove(os.path.join(path, ch, "basic radicals", ri))









if __name__ == '__main__':

    # clean extra image of radical
    clean_png_in_radicals(lp_processed)
    # parse xml file
    tree = ET.parse(xml_path)
    if tree is None:
        print("tree is none!")

    root = tree.getroot()
    print("root len:", len(root))

    # root = add_basic_radical_info_to_xml(root, char_775_path)
    # root = add_basic_radical_info_to_xml(root, char_1000_path)

    root = add_basic_radical_info_to_xml(root, lp_processed)

    prettyXml(root, '\t', '\n')
    tree.write(save_path, encoding='utf-8')
