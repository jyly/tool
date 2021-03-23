;eg0308.asm
	include io32.inc
	.data
ten	= 10
dvar	dword 67762000h,12345678h
	.code
start:
	mov eax,dvar+4
	push eax
	push dword ptr ten
	push dvar
	pop eax
	pop dvar+4
	mov ebx,dvar+4
	pop ecx
	call disprd

	exit 0
	end start
