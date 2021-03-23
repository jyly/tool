;eg0401.asm
	include io32.inc
	.data
nvar	dword ?
	.code
start:
	mov al,'0'
	call dispc
	jmp labl1
	nop
labl1:
	mov al,'1'
	call dispc
	jmp near ptr labl2
	nop
labl2:
	mov al,'2'
	call dispc
	mov eax,offset labl3
	jmp eax
	nop
labl3:
	mov al,'3'
	call dispc
	mov eax,offset labl4
	mov nvar,eax
	jmp nvar
	nop
labl4:	
	mov al,'4'
	call dispc
	exit 0
	end start
