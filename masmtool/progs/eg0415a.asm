;eg0415a.asm
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
	mov regd[ebx+4],al
	pop eax
	inc ebx
	dec ecx
	jnz again
	mov eax,offset regd
	call dispmsg	; ��ʾ

	exit 0
	; �ӳ���
htoasc	proc	; ��AL��4λ����һλʮ��������ת��ΪASCII��
	and eax,0fh	; ȡ��һλʮ��������
	mov al,ASCII[eax] 	; ����	
	ret
	; �ӳ���ľֲ�����
ASCII	byte '0123456789ABCDEF'
htoasc	endp
	
	end start