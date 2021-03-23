;eg0402b.asm
	include io32.inc
	.code
start:
	mov eax,887
	shr eax,1
	adc eax,0
	call dispuid

	exit 0
	end start