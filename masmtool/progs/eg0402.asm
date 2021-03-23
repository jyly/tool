;eg0402.asm
	include io32.inc
	.code
start:
	mov eax,885
	shr eax,1
	jnc goeven
	add eax,1
goeven:	call dispuid

	exit 0
	end start