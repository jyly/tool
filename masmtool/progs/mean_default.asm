	TITLE	D:\temp\mean\mean.cpp
	.386P
include listing.inc
if @Version gt 510
.model FLAT
else
_TEXT	SEGMENT PARA USE32 PUBLIC 'CODE'
_TEXT	ENDS
_DATA	SEGMENT DWORD USE32 PUBLIC 'DATA'
_DATA	ENDS
CONST	SEGMENT DWORD USE32 PUBLIC 'CONST'
CONST	ENDS
_BSS	SEGMENT DWORD USE32 PUBLIC 'BSS'
_BSS	ENDS
_TLS	SEGMENT DWORD USE32 PUBLIC 'TLS'
_TLS	ENDS
;	COMDAT ?lock@ios@@QAAXXZ
_TEXT	SEGMENT PARA USE32 PUBLIC 'CODE'
_TEXT	ENDS
;	COMDAT ?unlock@ios@@QAAXXZ
_TEXT	SEGMENT PARA USE32 PUBLIC 'CODE'
_TEXT	ENDS
;	COMDAT ?unlockbuf@ios@@QAAXXZ
_TEXT	SEGMENT PARA USE32 PUBLIC 'CODE'
_TEXT	ENDS
;	COMDAT ?gptr@streambuf@@IBEPADXZ
_TEXT	SEGMENT PARA USE32 PUBLIC 'CODE'
_TEXT	ENDS
;	COMDAT ?setf@ios@@QAEJJJ@Z
_TEXT	SEGMENT PARA USE32 PUBLIC 'CODE'
_TEXT	ENDS
;	COMDAT ?rdbuf@ios@@QBEPAVstreambuf@@XZ
_TEXT	SEGMENT PARA USE32 PUBLIC 'CODE'
_TEXT	ENDS
;	COMDAT ??4istream@@IAEAAV0@ABV0@@Z
_TEXT	SEGMENT PARA USE32 PUBLIC 'CODE'
_TEXT	ENDS
;	COMDAT ??6ostream@@QAEAAV0@P6AAAV0@AAV0@@Z@Z
_TEXT	SEGMENT PARA USE32 PUBLIC 'CODE'
_TEXT	ENDS
;	COMDAT ??6ostream@@QAEAAV0@D@Z
_TEXT	SEGMENT PARA USE32 PUBLIC 'CODE'
_TEXT	ENDS
;	COMDAT ?flush@@YAAAVostream@@AAV1@@Z
_TEXT	SEGMENT PARA USE32 PUBLIC 'CODE'
_TEXT	ENDS
;	COMDAT ?endl@@YAAAVostream@@AAV1@@Z
_TEXT	SEGMENT PARA USE32 PUBLIC 'CODE'
_TEXT	ENDS
;	COMDAT ??4iostream@@IAEAAV0@PAVstreambuf@@@Z
_TEXT	SEGMENT PARA USE32 PUBLIC 'CODE'
_TEXT	ENDS
FLAT	GROUP _DATA, CONST, _BSS
	ASSUME	CS: FLAT, DS: FLAT, SS: FLAT
endif
PUBLIC	?endl@@YAAAVostream@@AAV1@@Z			; endl
PUBLIC	?mean@@YAJQAJJ@Z				; mean
PUBLIC	_main
PUBLIC	??6ostream@@QAEAAV0@P6AAAV0@AAV0@@Z@Z		; ostream::operator<<
EXTRN	??6ostream@@QAEAAV0@J@Z:NEAR			; ostream::operator<<
EXTRN	?cout@@3Vostream_withassign@@A:BYTE		; cout
EXTRN	??6ostream@@QAEAAV0@PBD@Z:NEAR			; ostream::operator<<
_DATA	SEGMENT
$SG1291	DB	'The mean is ', 09H, 00H
_DATA	ENDS
_TEXT	SEGMENT
_array$ = -40
_main	PROC NEAR

; 6    : {

	push	ebp
	mov	ebp, esp
	sub	esp, 40					; 00000028H

; 7    :   long array[COUNT] = {675, 354, -34, 198, 267, 0, 9, 2371, -67, 4257};

	mov	DWORD PTR _array$[ebp], 675		; 000002a3H
	mov	DWORD PTR _array$[ebp+4], 354		; 00000162H
	mov	DWORD PTR _array$[ebp+8], -34		; ffffffdeH
	mov	DWORD PTR _array$[ebp+12], 198		; 000000c6H
	mov	DWORD PTR _array$[ebp+16], 267		; 0000010bH
	mov	DWORD PTR _array$[ebp+20], 0
	mov	DWORD PTR _array$[ebp+24], 9
	mov	DWORD PTR _array$[ebp+28], 2371		; 00000943H
	mov	DWORD PTR _array$[ebp+32], -67		; ffffffbdH
	mov	DWORD PTR _array$[ebp+36], 4257		; 000010a1H

; 8    :   cout<<"The mean is \t"<<mean(array,COUNT)<<endl;

	push	OFFSET FLAT:?endl@@YAAAVostream@@AAV1@@Z ; endl
	push	10					; 0000000aH
	lea	eax, DWORD PTR _array$[ebp]
	push	eax
	call	?mean@@YAJQAJJ@Z			; mean
	add	esp, 8
	push	eax
	push	OFFSET FLAT:$SG1291
	mov	ecx, OFFSET FLAT:?cout@@3Vostream_withassign@@A
	call	??6ostream@@QAEAAV0@PBD@Z		; ostream::operator<<
	mov	ecx, eax
	call	??6ostream@@QAEAAV0@J@Z			; ostream::operator<<
	mov	ecx, eax
	call	??6ostream@@QAEAAV0@P6AAAV0@AAV0@@Z@Z	; ostream::operator<<

; 9    :   return 0;

	xor	eax, eax

; 10   : }

	mov	esp, ebp
	pop	ebp
	ret	0
_main	ENDP
_d$ = 8
_num$ = 12
_i$ = -8
_temp$ = -4
?mean@@YAJQAJJ@Z PROC NEAR				; mean

; 12   : {

	push	ebp
	mov	ebp, esp
	sub	esp, 8

; 13   :   long i,temp=0;

	mov	DWORD PTR _temp$[ebp], 0

; 14   :   for(i=0; i<num; i++) temp=temp+d[i];

	mov	DWORD PTR _i$[ebp], 0
	jmp	SHORT $L1298
$L1299:
	mov	eax, DWORD PTR _i$[ebp]
	add	eax, 1
	mov	DWORD PTR _i$[ebp], eax
$L1298:
	mov	ecx, DWORD PTR _i$[ebp]
	cmp	ecx, DWORD PTR _num$[ebp]
	jge	SHORT $L1300
	mov	edx, DWORD PTR _i$[ebp]
	mov	eax, DWORD PTR _d$[ebp]
	mov	ecx, DWORD PTR _temp$[ebp]
	add	ecx, DWORD PTR [eax+edx*4]
	mov	DWORD PTR _temp$[ebp], ecx
	jmp	SHORT $L1299
$L1300:

; 15   :   temp=temp/num;

	mov	eax, DWORD PTR _temp$[ebp]
	cdq
	idiv	DWORD PTR _num$[ebp]
	mov	DWORD PTR _temp$[ebp], eax

; 16   :   return (temp);

	mov	eax, DWORD PTR _temp$[ebp]

; 17   : }

	mov	esp, ebp
	pop	ebp
	ret	0
?mean@@YAJQAJJ@Z ENDP					; mean
_TEXT	ENDS
;	COMDAT ??6ostream@@QAEAAV0@P6AAAV0@AAV0@@Z@Z
_TEXT	SEGMENT
__f$ = 8
_this$ = -4
??6ostream@@QAEAAV0@P6AAAV0@AAV0@@Z@Z PROC NEAR		; ostream::operator<<, COMDAT

; 112  : inline ostream& ostream::operator<<(ostream& (__cdecl * _f)(ostream&)) { (*_f)(*this); return *this; }

	push	ebp
	mov	ebp, esp
	push	ecx
	mov	DWORD PTR _this$[ebp], ecx
	mov	eax, DWORD PTR _this$[ebp]
	push	eax
	call	DWORD PTR __f$[ebp]
	add	esp, 4
	mov	eax, DWORD PTR _this$[ebp]
	mov	esp, ebp
	pop	ebp
	ret	4
??6ostream@@QAEAAV0@P6AAAV0@AAV0@@Z@Z ENDP		; ostream::operator<<
_TEXT	ENDS
PUBLIC	?flush@@YAAAVostream@@AAV1@@Z			; flush
PUBLIC	??6ostream@@QAEAAV0@D@Z				; ostream::operator<<
;	COMDAT ?endl@@YAAAVostream@@AAV1@@Z
_TEXT	SEGMENT
__outs$ = 8
?endl@@YAAAVostream@@AAV1@@Z PROC NEAR			; endl, COMDAT

; 144  : inline _CRTIMP ostream& __cdecl endl(ostream& _outs) { return _outs << '\n' << flush; }

	push	ebp
	mov	ebp, esp
	push	OFFSET FLAT:?flush@@YAAAVostream@@AAV1@@Z ; flush
	push	10					; 0000000aH
	mov	ecx, DWORD PTR __outs$[ebp]
	call	??6ostream@@QAEAAV0@D@Z			; ostream::operator<<
	mov	ecx, eax
	call	??6ostream@@QAEAAV0@P6AAAV0@AAV0@@Z@Z	; ostream::operator<<
	pop	ebp
	ret	0
?endl@@YAAAVostream@@AAV1@@Z ENDP			; endl
_TEXT	ENDS
EXTRN	??6ostream@@QAEAAV0@E@Z:NEAR			; ostream::operator<<
;	COMDAT ??6ostream@@QAEAAV0@D@Z
_TEXT	SEGMENT
__c$ = 8
_this$ = -4
??6ostream@@QAEAAV0@D@Z PROC NEAR			; ostream::operator<<, COMDAT

; 115  : inline  ostream& ostream::operator<<(char _c) { return operator<<((unsigned char) _c); }

	push	ebp
	mov	ebp, esp
	push	ecx
	mov	DWORD PTR _this$[ebp], ecx
	mov	al, BYTE PTR __c$[ebp]
	push	eax
	mov	ecx, DWORD PTR _this$[ebp]
	call	??6ostream@@QAEAAV0@E@Z			; ostream::operator<<
	mov	esp, ebp
	pop	ebp
	ret	4
??6ostream@@QAEAAV0@D@Z ENDP				; ostream::operator<<
_TEXT	ENDS
EXTRN	?flush@ostream@@QAEAAV1@XZ:NEAR			; ostream::flush
;	COMDAT ?flush@@YAAAVostream@@AAV1@@Z
_TEXT	SEGMENT
__outs$ = 8
?flush@@YAAAVostream@@AAV1@@Z PROC NEAR			; flush, COMDAT

; 143  : inline _CRTIMP ostream& __cdecl flush(ostream& _outs) { return _outs.flush(); }

	push	ebp
	mov	ebp, esp
	mov	ecx, DWORD PTR __outs$[ebp]
	call	?flush@ostream@@QAEAAV1@XZ		; ostream::flush
	pop	ebp
	ret	0
?flush@@YAAAVostream@@AAV1@@Z ENDP			; flush
_TEXT	ENDS
END
