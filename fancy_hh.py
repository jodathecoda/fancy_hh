import os
from datetime import datetime


cwd = os.getcwd()

suit_spade = '\u2660'
suit_heart = '\u2665'
suit_diamond = '\u2666'
suit_club = '\u2663'

original_codecs =['As', 'Ah', 'Ad', 'Ac', \
                  'Ks', 'Kh', 'Kd', 'Kc', \
                  'Qs', 'Qh', 'Qd', 'Qc', \
                  'Js', 'Jh', 'Jd', 'Jc', \
                  'Ts', 'Th', 'Td', 'Tc', \
                  '9s', '9h', '9d', '9c', \
                  '8s', '8h', '8d', '8c', \
                  '7s', '7h', '7d', '7c', \
                  '6s', '6h', '6d', '6c', \
                  '5s', '5h', '5d', '5c', \
                  '4s', '4h', '4d', '4c', \
                  '3s', '3h', '3d', '3c', \
                  '2s', '2h', '2d', '2c', \
                  ]

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

replace_dictionary = {'As': 'A' + suit_spade, 'Ah': 'A' + suit_heart, 'Ad': 'A' + suit_diamond, 'Ac': 'A' + suit_club, \
                      'Ks': 'K' + suit_spade, 'Kh': 'K' + suit_heart, 'Kd': 'K' + suit_diamond, 'Kc': 'K' + suit_club, \
                      'Qs': 'Q' + suit_spade, 'Qh': 'Q' + suit_heart, 'Qd': 'Q' + suit_diamond, 'Qc': 'Q' + suit_club, \
                      'Js': 'J' + suit_spade, 'Jh': 'J' + suit_heart, 'Jd': 'J' + suit_diamond, 'Jc': 'J' + suit_club, \
                      'Ts': 'T' + suit_spade, 'Th': 'T' + suit_heart, 'Td': 'T' + suit_diamond, 'Tc': 'T' + suit_club, \
                      '9s': '9' + suit_spade, '9h': '9' + suit_heart, '9d': '9' + suit_diamond, '9c': '9' + suit_club, \
                      '8s': '8' + suit_spade, '8h': '8' + suit_heart, '8d': '8' + suit_diamond, '8c': '8' + suit_club, \
                      '7s': '7' + suit_spade, '7h': '7' + suit_heart, '7d': '7' + suit_diamond, '7c': '7' + suit_club, \
                      '6s': '6' + suit_spade, '6h': '6' + suit_heart, '6d': '6' + suit_diamond, '6c': '6' + suit_club, \
                      '5s': '5' + suit_spade, '5h': '5' + suit_heart, '5d': '5' + suit_diamond, '5c': '5' + suit_club, \
                      '4s': '4' + suit_spade, '4h': '4' + suit_heart, '4d': '4' + suit_diamond, '4c': '4' + suit_club, \
                      '3s': '3' + suit_spade, '3h': '3' + suit_heart, '3d': '3' + suit_diamond, '3c': '3' + suit_club, \
                      '2s': '2' + suit_spade, '2h': '2' + suit_heart, '2d': '2' + suit_diamond, '2c': '2' + suit_club
                      }

def replace_card(input_line):
  new_line = replace_all(input_line, replace_dictionary)
  '''
  As_rep = ""
  Ah_rep = ""
  if "As" in in_line:
    As_rep = in_line.replace('As', 'A\u2660')
  if "Ah" in As_rep:
    Ah_rep = As_rep.replace('Ah', 'A\u2665')
  '''
  return new_line

weirdInput = "hello \\ud83d\\ude04".encode("latin_1")

'''
output = (weirdInput
    .decode("raw_unicode_escape")
    .encode('utf-16', 'surrogatepass')
    .decode('utf-16')
    .encode("raw_unicode_escape")
    .decode("latin_1")
  )
'''

smiley = (weirdInput
  .decode("raw_unicode_escape")
  .encode('utf-16', 'surrogatepass')
  .decode('utf-16')
)

#print(output)
#print(smiley)

#f = open("demofile2.txt", "a", encoding = 'utf-16')
#f.write(smiley)
#f.close()

for filename in os.listdir(cwd):
  #print(file)
  if filename.endswith("log"):
    #open file for writing, code it with timestamp to be unique
    #remove . and :from atring
    now = str(datetime.now().time()).replace(':', '').replace('.', '')
    f_writing = open("hh" + now + ".txt", "w", encoding = "utf-16")
    f_reading = open(filename, "r")
    lines = f_reading.readlines()
    f_reading.close()
    for l in lines:
      f_writing.write(replace_card(l))
    f_writing.close()

