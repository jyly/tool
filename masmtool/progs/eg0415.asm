;eg0415.asm
	include io32.inc
	.data
regd	byte 'EAX=',8 dup(0),'H',0
	.code
start:
	mov eax,1234abcdh
	xor ebx,ebx
	mov ecx,8	; 8λʮ��������
again:	rol eax,4
	push eax
	call htoasc	; �����ӳ���
	mov regd+4[ebx],al
	pop eax
	inc ebx
	dec ecx
	jnz again
	mov eax,offset regd
	call dispmsg	; ��ʾ

	exit 0
	; �ӳ���
htoasc	proc	; ���̶��壬������Ϊhtoasc
	and al,0fh	; ֻȡAL�ĵ�4λ
	or al,30h	; AL��4λ���3
	cmp al,39h	; ��0��9������A��F
	jbe htoend
	add al,7	; ��A��F����ASCII���ټ���7
htoend:	ret	; �ӳ��򷵻�
htoasc	endp	; ���̽���
	
	end start