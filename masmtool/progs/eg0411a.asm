;eg0411a.asm
	include io32.inc
	.data
key	byte 234
buffer	byte '���ܿ�������Can you see me?',0	
msg2	byte 'Encrypted message: ',0
msg3	byte 13,10,'Original messge: ',0
	.code
start:
	mov eax,lengthof buffer-1
	push eax	; �ַ�������������ջ
	mov ecx,eax	; ECX��ʵ��������ַ���������Ϊѭ���Ĵ���
	xor ebx,ebx	; EBXָ�������ַ�
encrypt:	mov al,key	; AL�����ܹؼ���
	xor buffer[ebx],al	; ������
	inc ebx
	dec ecx	; ��ͬ��ָ�loop encrypt
	jnz encrypt	; ������һ���ַ�
	mov eax,offset msg2
	call dispmsg
	mov eax,offset buffer	; ��ʾ���ܺ������
	call dispmsg
	;
	pop ecx	; �Ӷ�ջ�����ַ���������Ϊѭ���Ĵ���
	xor ebx,ebx	; EBXָ�������ַ�
decrypt:	mov al,key	; AL�����ܹؼ���
	xor buffer[ebx],al	; ������
	inc ebx
	dec ecx
	jnz decrypt	; ������һ���ַ�
	mov eax,offset msg3
	call dispmsg
	mov eax,offset buffer	; ��ʾ���ܺ������
	call dispmsg

	exit 0
	end start