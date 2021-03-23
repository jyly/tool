;eg0312.asm
	include io32.inc
	.data
msg	byte 'welcome',0
	.code
start:
	mov ecx,(lengthof msg)-1
	mov ebx,0
again:	sub msg[ebx],'a'-'A'
	inc ebx
	loop again
	mov eax,offset msg
	call dispmsg
	
	exit 0
	end start
