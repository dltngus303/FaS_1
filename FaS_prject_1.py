import sys
import argparse
import os
import struct
import shutil
import binascii


f = open('C:/Users/gus98/Desktop/A.zip', 'rb')
f.seek(0)

local_1_signature = f.read(4)
local_1_version = f.read(2)
local_1_flags = f.read(2)
local_1_compressed_method = f.read(2)
local_1_modified_time = f.read(2)
local_1_modified_year = f.read(2)
local_1_crc = f.read(4)
local_1_compressed_size = f.read(4)
local_1_not_compressed_size = f.read(4)
local_1_f_name_length = f.read(2)
local_1_extra_field_length = f.read(2)
local_1_f_name = f.read(5)

f.seek(74)

local_2_signature = f.read(4)
local_2_version = f.read(2)
local_2_flags = f.read(2)
local_2_compressed_method = f.read(2)
local_2_modified_time = f.read(2)
local_2_modified_year = f.read(2)
local_2_crc = f.read(4)
local_2_compressed_size = f.read(4)
local_2_not_compressed_size = f.read(4)
local_2_f_name_length = f.read(2)
local_2_extra_field_length = f.read(2)
local_2_f_name = f.read(5)

print(local_1_f_name, local_2_f_name, ' ')
print(binascii.hexlify(local_1_signature), binascii.hexlify(local_2_signature), ' ')