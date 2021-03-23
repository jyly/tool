;eg0310.asm
	include io32.inc
	.data
dvar	dword 41424344h
	.code
start:
	mov eax,dvar
	lea esi,dvar
	mov ebx,[esi]
	mov edi,offset dvar
	mov ecx,[edi]
	lea edx,[esi+edi*4+100h]
	call disprd

	exit 0
	end start