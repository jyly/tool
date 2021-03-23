;eg0401.asm
	include io32.inc
	.data
nvar	dword ?
	.code
start:
	jmp labl1
	nop
labl1:	jmp near ptr labl2
	nop
labl2:	mov eax,offset labl3
	jmp eax
	nop
labl3:	mov eax,offset labl4
	mov nvar,eax
	jmp nvar
	nop
labl4:	
	exit 0
	end start
