;eg0201a.asm
	include io32.inc
WriteString	macro msg
	mov eax,offset msg		;��ʾ
	call dispmsg
	endm
	.data
msg    byte 'Hello, Assembly !',13,10,0	;�ַ���
	.code
start:

	WriteString msg
	exit 0
	end start