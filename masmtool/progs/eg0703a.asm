;eg0703a.asm in Win32 Console
	include io32.inc
	.data
msg	byte 0dh,0ah,'No divide overflow !',0
	.code
start:

	call readuiw
	mov bl,1
	div bl
	mov eax,offset msg
	call dispmsg
	exit 0
	end start
