;eg0316b.asm
	include io32.inc
	.data
srcmsg	byte 'In a major matter, no details are small.',0	
destmsg byte (lengthof srcmsg) dup (0)
	.code
start:
	mov esi,offset srcmsg
	mov edi,offset destmsg
	mov ecx,lengthof srcmsg

again:	mov al,[esi] 	; ��Դ�ַ���ȡһ���ַ�
	mov [edi],al	; ���͵�Ŀ���ַ���
	add esi,1	; ��ַ����
	add edi,1	; ָ����һ���ַ�
	loop again	; �ظ������ַ�������

	mov eax, offset destmsg
	call dispmsg
	
	exit 0
	end start