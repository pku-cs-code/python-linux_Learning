sentence = raw_input('Sentence:')

screen_width = 80
text_width =  len(sentence)
box_width = 6+ text_width + 6
left_margin = (screen_width-box_width)//2
e = (box_width-text_width-2)//2

#print '*'*screen_width
print ' '*left_margin + '+' + '-'*(box_width-2) + '+'
print ' '*(left_margin)+ '|' + ' '*e +' '*text_width + ' '*e+ '|'
print ' '*(left_margin)+ '|' +' '*e + sentence + ' '*e+ '|'
print ' '*(left_margin)+ '|' + ' '*e +' '*text_width + ' '*e+ '|'

print ' '*left_margin + '+' + '-'*(box_width-2) + '+'
print
