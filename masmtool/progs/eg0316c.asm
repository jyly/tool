;eg0316c.asm
	include io32.inc
	.data
srcmsg	byte 'In a major matter, no details are small.',0	
destmsg byte (lengthof srcmsg) dup (0)
	.code
start:
	xor ebx,ebx	; EBX��0
	mov ecx,lengthof srcmsg	; ECX���ַ�������
again:	mov al,srcmsg[ebx]	; ��Դ�ַ���ȡһ���ַ�
	mov destmsg[ebx],al	; ���͵�Ŀ���ַ���
	inc ebx		; ָ����һ���ַ�
	loop again	; �ظ������ַ�������

	mov eax, offset destmsg
	call dispmsg
	
	exit 0
	end start