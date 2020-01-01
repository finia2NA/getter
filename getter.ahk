^0::
send, ^a
Sleep, 10
send, ^c
Sleep, 10
send, {Delete}
; send, ^{Right}
Run, python getter.py -c "'"%Clipboard%"'"
