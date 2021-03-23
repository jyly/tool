;eg0402c.asm
	include io32.inc
	.code
start:
	mov eax,888
	add eax,1
	rcr eax,1
	call dispuid

	exit 0
	end start