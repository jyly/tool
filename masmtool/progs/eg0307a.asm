;eg0307a.asm
	include io32.inc
	.data
num	byte 6,7,7,8,3,0,0,0
tab	byte '67783000'
	.code
start:
	mov ecx,lengthof num
	mov esi,0
again:	mov al,num[esi]
	xchg al,tab[esi]
	mov num[esi],al
	call dispc
	add esi,1
	loop again

	exit 0
	end start
