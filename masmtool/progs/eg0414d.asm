;eg0414d.asm
	include io32.inc
	.data

	.code
start:
	mov eax,1
	mov ebp,5
	push offset retp1	; call subp
	jmp subp

retp1:	mov ecx,3
retp2:	mov edx,4
	call disprd

	exit 0
subp	proc	; ���̶��壬������Ϊsubp
	push ebp
	mov ebp,esp
	mov esi,[ebp+4]
	mov edi,offset retp2
	mov ebx,2
	pop ebp	; ������ջ�����ֶ�ջƽ��

	add esp,4	; �ӳ��򷵻�(ret)
	jmp dword ptr [esp-4]

subp	endp	; ���̽���
	
	end start