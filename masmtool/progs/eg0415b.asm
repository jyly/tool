;eg0415b.asm
	include io32.inc
	.data
regd	byte 'EAX=',8 dup(0),'H',0
	.code
start:
	mov eax,1234abcdh
	mov ebx,4
	mov ecx,8	; 8λʮ��������
again:	rol eax,4
	push eax
	call htoasc	; �����ӳ���
	mov regd[ebx],al
	pop eax
	inc ebx
	dec ecx
	jnz again
	mov eax,offset regd
	call dispmsg	; ��ʾ

	exit 0
	; �ӳ���
htoasc	proc	; ��AL��4λ����һλʮ��������ת��ΪASCII��
	push ebx
	mov ebx,offset ASCII 
	and al,0fh	; ȡ��һλʮ��������
	xlat ASCII	; ���룺AL��CS:[EBX��AL]��ע�������ڴ����CS
	pop ebx
	ret
	; �ӳ���ľֲ�����
ASCII	byte '0123456789ABCDEF'
htoasc	endp
	
	end start