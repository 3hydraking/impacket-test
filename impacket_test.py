#!/usr/bin/python

import struct
import time
import sys

from threading import Thread #Thread is imported incase you would like to modify

from impacket import smb
from impacket import uuid
from impacket import dcerpc
from impacket.dcerpc.v5 import transport

print('works')
