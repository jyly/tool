;eg0704a.asm in Win32 Console
	include io32.inc
	.data
msg	byte 0dh,0ah,'No overflow !',0
	.code
start:
	call readuib
	add al,100
	jno noflow
	into
	jmp done
noflow:	mov eax,offset msg
	call dispmsg
done:	exit 0
	end start
