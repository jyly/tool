include io32.inc
; .data
	; TAB dword 0,1,4,9,16,25,36,49,64,81
	; T1 dword 6
	; T2 dword ?
; .code
; start:
	; mov eax,T1
	; mov eax,TAB[eax*(type TAB)]
	; call dispuid
	; exit 0
	; end start

.data
	array1 dword 1,2,3,4,5,6,7,8
	array2 dword 1,2,3,9,10,11,12,4,5,6,7,8
	array3 dword ?
.code
start:
	xor eax,eax
	mov ebx,eax
	mov ecx,eax
outloop:
	mov eax,array1[ebx*(type array1)]
	shr eax,1
	jnc endc
	inc ebx
	cmp ebx,8
	jc outloop
endc:
	mov eax,array1[ebx*(type array1)]
	xor edx,edx
inloop:
	cmp eax,array2[edx*(type array2)]
	jz getin
	inc edx
	cmp edx,12
	jc inloop
	inc ebx
	cmp ebx,8
	jc outloop
getin:	
	mov array3[ecx*(type array3)],eax
	inc ecx
	inc ebx
	cmp ebx,8
	jc outloop
	xor eax,eax
	mov ebx,eax
print:
	mov eax,array3[ebx*(type array3)]
	call dispsid
	call dispcrlf
	inc ebx
	cmp ebx,ecx
	jc print
	exit 0
	end start
	