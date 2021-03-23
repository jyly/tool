;eg0420s.asm���ӳ����ļ���
	include io32.inc
	public read, write, mean	; �ӳ�����
	extern temp:dword	; �ⲿ����
	.data
writebuf	byte 12 dup(0)	; ��ʾ������
readbuf		byte 30 dup(0)

	.code
write	proc c	; ��ʾ�з���ʮ���������ӳ���EAX����ڲ���
	push ebx	; �����Ĵ���
	push ecx
	push edx
	mov ecx,sizeof writebuf-1	; ��ʾ��������0
write0:	mov writebuf[ecx],0
	sub ecx,1
	jnc write0
	mov ebx,offset writebuf	; EBXָ����ʾ������
	test eax,eax	; �ж��������㡢��������
	jnz write1	; �����㣬��ת
	mov byte ptr [ebx],'0'	; ���㣬����"0"
	jmp write5	; ת����ʾ
write1:	jns write2	; ����������ת
	mov byte ptr [ebx],'-'	; �Ǹ��������ø���"��"
	inc ebx
	neg eax	; �����󲹣�����ֵ��
write2:	mov ecx,10
	push ecx	; 10ѹ���ջ����Ϊ�˳���־
write3:	cmp eax,0	; ���ݣ��̣�Ϊ�㣬ת�򱣴�
	jz write4 
	xor edx,edx	; ��λ��չ������ΪEDX.EAX
	div ecx	; ���ݳ���10��EDX.EAX��10
	add edx,30h	; ������0��9��ת��ΪASCII��
	push edx	; ���ݸ�λ�ȵ�λ���λѹ���ջ
	jmp write3
write4:	pop edx	; ���ݸ�λ�ȸ�λ���λ������ջ
	cmp edx,ecx	; �ǽ�����־10��ת����ʾ
	je write5
	mov [ebx],dl	; ���ݱ��浽������
	inc ebx
	jmp write4
write5:	mov eax,offset writebuf
	call dispmsg
	pop edx	; �ָ��Ĵ���
	pop ecx
	pop ebx
	ret	; �ӳ��򷵻�
write	endp

read	proc c	; �����з���ʮ���������ӳ���
	push eax	; ���ڲ���������TEMP�������ʾ�Ķ�������ֵ
	push ebx	; ˵����������"��"����
	push ecx
	push edx
read0:	mov eax,offset readbuf
	call readmsg	; ����һ���ַ���
	test eax,eax
	jz readerr	; û���������ݣ�ת�������
	cmp eax,12
	ja readerr	; ���볬��12���ַ���ת�������
	mov edx,offset readbuf	; EDXָ�����뻺����
	xor ebx,ebx	; EBX������
	xor ecx,ecx	; ECXΪ������־��0Ϊ������1Ϊ��
	mov al,[edx]	; ȡһ���ַ�
	cmp al,'+'	; ��"��"������
	jz read1
	cmp al,'-'	; ��"��"�����ã�1��־
	jnz read2
	mov ecx,-1
read1:	inc edx	; ȡ��һ���ַ�
	mov al,[edx]
	test al,al	; �ǽ�β0��ת������
	jz read3
read2:	cmp al,'0'	; ����0��9֮������룬���������
	jb readerr
	cmp al,'9'
	ja readerr
	sub al,30h	; ��0��9֮������룬��ת��Ϊ��������
	imul ebx,10	; ԭ��ֵ��10��EBX��EBX��10
	jc readerr	; CF��1��˵���˻�������������ݳ���32λ��Χ������
	movzx eax,al	; ��λ��չ���������
	add ebx,eax	; ԭ��ֵ��10�������������
	jnc read1	; CF��0������ת����һ����λ
		; CF��1��˵���������ݳ���32λ��Χ������
readerr:	mov eax,offset errmsg
	call dispmsg
	jmp read0
	;
read3:	test ecx,ecx	; �ж����������Ǹ���
	jz read4
	cmp ebx,80000000h	; ��������231������
	ja readerr
	neg ebx	; �Ǹ�����������
	jmp read5
read4:	cmp ebx,7fffffffh	; ��������231-1������
	ja readerr
read5:	mov temp,ebx	; ���ó��ڲ���
	pop edx
	pop ecx
	pop ebx
	pop eax
	ret	; �ӳ��򷵻�
errmsg	byte 'Input error, enter again: ',0
read	endp

mean	proc c	; ����32λ�з�����ƽ��ֵ�ӳ���
	push ebp	; ��ڲ�����˳��ѹ�����ݸ���������ƫ�Ƶ�ַ
	mov ebp,esp	; ���ڲ�����EAX��ƽ��ֵ
	push ebx	; �����Ĵ���
	push ecx
	push edx
	mov ebx,[ebp+8]	; EBX����ջ��ȡ����ƫ�Ƶ�ַ
	mov ecx,[ebp+12]	; ECX����ջ��ȡ�������ݸ���
	xor eax,eax	; EAX�����ֵ
	xor edx,edx	; EDX��ָ������Ԫ��
mean1:	add eax,[ebx+edx*4]	; ���
	add edx,1	; ָ����һ������
	cmp edx,ecx	; �Ƚϸ���
	jb mean1	; ѭ��
	cdq	; ���ۼӺ�EAX������չ��EDX
	idiv ecx	; �з�����������EAX��ƽ��ֵ��������EDX�У�
	pop edx	; �ָ��Ĵ���
	pop ecx
	pop ebx
	pop ebp
	ret
mean	endp

	end
