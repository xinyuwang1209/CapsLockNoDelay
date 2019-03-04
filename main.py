#!python3

#Author: Xinyu Wang

import os
import subprocess

if os.path.exists('/tmp/CapsLockNoDelay'):
	print("Caps Lock has already been fixed!")
else:
	print('Export your keyboard configurations to a file: ', end='')
	DISPLAY = os.environ['DISPLAY']
	cmd = ["xkbcomp", "-xkb", DISPLAY, "xkbmap"]
	subprocess.run(cmd, stdout=subprocess.PIPE)
	print('Completed!')

	print('Locate and replace Caps Lock Configuration in xkbmap:', end='')
	key_word = 'key <CAPS>'
	replace = '''key <CAPS> {
	    repeat=no,
	    type[group1]="ALPHABETIC",
	    symbols[group1]=[ Caps_Lock, Caps_Lock],
	    actions[group1]=[ LockMods(modifiers=Lock), Private(type=3,data[0]=1,data[1]=3,data[2]=3)]
	};'''


	f = open('xkbmap', 'r')
	lines = f.readlines()
	g = open('xkbmap', 'w')
	f.close()

	i=0
	len_lines = len(lines)
	while i < len_lines:
		line = lines[i]
		if key_word in line:
			lines[i] = replace
	#		for j in range(10):
	#			print('current:', lines[i+j])
	#		lines[i+1] = '''	repeat=no,'''
	#		lines[i+2] = '''	type[group1]="ALPHABETIC",'''
	#		lines[i+3] = '''	symbols[group1]=[ Caps_Lock, Caps_Lock],'''
	#		lines[i+4] = '''	actions[group1]=[ LockMods(modifiers=Lock), Private(type=3,data[0]=1,data[1]=3,data[2]=3)]'''
			break
		i += 1
		
	g.writelines(lines)
	g.close()
	print('Completed!')

	print('Save and reload keyboard configurations: ', end='')
	cmd = ['xkbcomp', '-w', '0', 'xkbmap', DISPLAY]
	subprocess.run(cmd, stdout=subprocess.PIPE)
	os.remove('xkbmap')
	print('Completed!')
