;eg0420.asm���������ļ���
	include io32.inc
	extern read:near,write:near,mean:near	; �ⲿ�ӳ���
	public temp	; ��������
	.data
count	= 10
array	dword count dup(0)
temp	dword ?
msg1	byte 'Enter 10 numbers: ',13,10,0
msg2	byte 'The mean is: ',0
	.code
start:
	mov eax,offset msg1	; ��ʾ����10������
	call dispmsg
	xor ebx,ebx 
	mov ecx,count	; ECX�����ݸ���
again:	call read	; �����ӳ�������һ������
	mov eax,temp	; ��ó��ڲ���
	mov array [ebx*4],eax 
	add ebx,1
	cmp ebx,count
	jb again
	push ecx	; ���ݲ���
	push offset array
	call mean	; �����ӳ�����ƽ��ֵ
	add esp,8
	mov ebx,eax	; EAX����ֵת�浽EBX
	mov eax,offset msg2	; ��ʾ���ƽ��ֵ
	call dispmsg 
	mov eax,ebx	; ��ʾ���ƽ��ֵ
	call write	; �����ӳ�����ʾƽ��ֵ
	exit 0
	end start
