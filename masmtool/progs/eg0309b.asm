;eg0309b.asm
	include io32.inc
	.data
num	byte 6,7,7,8,3,0,0,0
tab	byte '0123456789'
	.code
start:
	mov ecx,lengthof num
	mov esi,offset num
again:	mov eax,0
	mov al,[esi]
	mov al,tab[eax]
	call dispc
	add esi,1
	loop again

	exit 0
	end start
