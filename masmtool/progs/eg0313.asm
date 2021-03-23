;eg0313.asm
	include io32.inc
	.data
varA	dword 11001010000111100101010101001101b
varB	dword 00110111010110100011010111100001b
varT1	dword ?
varT2	dword ?
	.code
start:
	mov eax,varA
	not eax
	and eax,varB
	mov ebx,varB
	not ebx
	and ebx,varA
	or eax,ebx
	mov varT1,eax
	;
	mov eax,varA
	xor eax,varB
	mov varT2,eax
	;
	mov eax,varT1
	call dispbd
	call dispcrlf
	mov eax,varT2
	call dispbd
	
	exit 0
	end start
