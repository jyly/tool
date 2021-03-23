;eg0314.asm
	include io32.inc
	.data
wvar	word 34000
	.code
start:
	xor eax,eax
	mov ax,wvar
	shl eax,1	;*2
	mov ebx,eax
	shl eax,2	;*8
	add eax,ebx	;*10
	call dispuid
	call dispcrlf
	imul eax,10	;*10
	call dispuid

	exit 0
	end start