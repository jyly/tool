;eg0801.asm in DOS
	include io16.inc
	.data
freq	word 1193180/600	;��һ��600Hz��Ƶ��
	.code
start:
	mov ax,@data
	mov ds,ax
	mov ax,freq
	call speaker	;����������������
	call speakon	;������������
	call readc	;�ȴ�����

	call speakoff	;�ر�����������
	exit 0
	;����Ƶ�������ӳ�����ڲ�����AX��1.19318��106�·���Ƶ��
speaker	proc
	push ax	;�ݴ���ڲ������ⱻ�ƻ�
	mov al,0b6h	;��ʱ��2Ϊ��ʽ3���ȵͺ��д��16λ����ֵ
	out 43h,al
	pop ax	;�ָ���ڲ���
	out 42h,al	;д���8λ����ֵ
	mov al,ah
	out 42h,al	;д���8λ����ֵ
	ret
speaker	endp
speakon	proc	;���������ӳ���
	push ax
	in al,61h	;��ȡ61H�˿ڵ�ԭ������Ϣ
	or al,03h	;D1D0��PB1PB0��11������λ����
	out 61h,al	;ֱ�ӿ��Ʒ���
	pop ax
	ret
speakon	endp
speakoff	proc	;���������ӳ���
	push ax
	in al,61h
	and al,0fch	;D1D0��PB1PB0��00������λ���� 
	out 61h,al	;ֱ�ӿ��Ʊ���
	pop ax
	ret
speakoff	endp

	end start
