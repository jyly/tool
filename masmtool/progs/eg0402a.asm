;eg0402a.asm
	include io32.inc
	.code
start:
	mov eax,886
	shr eax,1
	jc goodd
	jmp goeven
goodd:	add eax,1
goeven:	call dispuid

	exit 0
	end start