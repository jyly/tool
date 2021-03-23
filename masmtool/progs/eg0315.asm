;eg0315.asm
	include io32.inc
	.data
qvar	qword 1234567887654321h
ascii	byte '38'
bcd	byte ?
	.code
start:
	mov ecx,4
again:	shr dword ptr qvar+4,1
	rcr dword ptr qvar,1
	loop again
	;
	mov al,ascii
	and al,0fh
	mov ah,ascii+1
	shl ah,4
	or al,ah
	mov bcd,al

	exit 0
	end start
