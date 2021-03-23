;eg0802.asm in DOS
	include io16.inc
	.data
buffer	byte 10 dup(0)	;���̻�����
bufptr1	word 0	;����ͷָ��
bufptr2	word 0	;����βָ��
	;��ɨ����˳������ַ���ASCII�루�µ�����Сд��ĸ����������ʾ�İ���Ϊ0
	;��һ��0����Ӧ�����������ڲ��ָ��
scantb	byte 0,1,'1234567890-=',08h	;���̵�1�ŵİ�������ESC���˸�
	byte 0,'qwertyuiop[]',0dh	;���̵�2�ŵİ�������Tab���س�
	byte 0,'asdfghjkl;',27h,'`'	;���̵�3�ŵİ�������Ctrl����`������
	byte 0,'\zxcvbnm,./',0,'*'	;���̵�4�ŵİ�������SHIFT����*������
	byte 0,20h,0,10 dup(0)	;ALT���ո�Caps Lock��10�����ܼ�
	byte 0,0,'789-456+1230.'	;�ұ�С���̣���Num Lock��Del
	.code
start:
	mov ax,@data
	mov ds,ax
	mov ax,3509h	; ��ȡ������09H��ԭ�ж�����
	int 21h
	push es
	push bx
	cli	; ���ж�
	push ds	; ����09H�����ж�����
	mov ax,seg kbint
	mov ds,ax
	mov dx,offset kbint
	mov ax,2509h
	int 21h
	pop ds
	in al,21h	; ����IRQ1�жϣ���������
	push ax
	and al,0fdh
	out 21h,al
	sti	; ���ж�
start1:	call kbget	; ����KBGET��ȡ������ASCII��
	cmp al,1
	jz start2	; ��ESC�������˳�
	push ax	; �����ַ�
	call dispc	; ��ʾ�ַ�
	pop ax	; �ָ��ַ�
	cmp al,0dh	; ���ַ��ǻس�����
	jnz start1	; ���ǣ���ȡ��һ�������ַ�
	mov al,0ah	; �ǻس��������ٽ��л���
	call dispc
	jmp start1	; ����ȡ�ַ�
start2:	cli	; �ָ��ж����μĴ������ж�����
	pop ax
	out 21h,al
	pop dx
	pop ds
	mov ax,2509h
	int 21h
	sti

	exit 0

kbget	proc
	push bx	; ����BX
kbget1:	cli	; ���жϣ��Է�ֹ�Ի���������ʱ�����ж��ֶԻ���������
	mov bx,bufptr1	; ȡ����������ͷָ��
	cmp bx,bufptr2	; ��βָ����ȷ�
	jnz kbget2	; ����ȣ�˵�����������ַ���ת��
	sti	; ��ȣ�˵���������գ����ж�
	jmp kbget1	; �ȴ����������ַ�
kbget2:	mov al,buffer[bx]	; �Ӷ���ͷȡ���ַ���AL
	inc bx	; ����ͷָ������
	cmp bx,10	; ָ���Ƿ�ָ�����ĩ�ˣ�
	jc kbget3	; û�У�ת��
	mov bx,0	; ָ��ָ�����ĩ�ˣ���ѭ����ָ��ʼ��
kbget3:	mov bufptr1,bx	; �趨�µĶ���ͷָ��
	sti	; ���ж�
	pop bx	; �ָ�BX
	ret	; �ӳ��򷵻�
kbget	endp
	; KBINT�жϷ��������09H�ż����ж�
kbint	proc
	sti	; ���ж�
	push ax	; �����Ĵ���
	push bx
	in al,60h	; ��ȡ����ɨ����
	mov bl,al	; ɨ���뱣����BL
	in al,61h	; ʹPB7��1����Ӧ����
	or al,80h
	out 61h,al
	and al,7fh	; ʹPB7��0���������
	out 61h,al
	test bl,80h	; �������ݴ���
	jnz kbint2	; �ǶϿ�ɨ���룬תKBINT2�˳�
	xor bh,bh
	mov al,scantb[bx]	; �ǽ�ͨɨ���룬ת����ASCII��
	cmp al,0	; �Ƿ�Ϊ�Ϸ���ASCII�룿
	jz kbint2	; ���ǣ���תKBINT2�˳�
	mov bx,bufptr2	; �ǣ�ȡ����βָ��
	mov buffer[bx],al	; ��ASCII����뻺��������β
	inc bx	; ����βָ������
	cmp bx,10	; ָ���Ƿ�ָ�����ĩ�ˣ�
	jc kbint1	; û�У�ת��
	mov bx,0	; ָ��ָ�����ĩ�ˣ���ѭ����ָ��ʼ��
kbint1:	cmp bx,bufptr1	; �������Ƿ�������
	jz kbint2 	; �������������˳�
	mov bufptr2,bx	; ���в����������µĶ���βָ��
kbint2:	mov al,20h	; ���жϿ�����������ͨ�жϽ�������
	out 20h,al
	pop bx	; �ָ��Ĵ���
	pop ax
	iret	; �жϷ���
kbint	endp

	end start
