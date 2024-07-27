.data
	array: .space 12 # allocate 12 bytes which is equal to 3 words
	# Data allocation starts from an offset divisible by 4
	# 6 bytes are allocated for asciiz
	# If you try to put a word in an offset that is not divisible by 4, an error will occur
	
	initializedArray: .word 100:3 # Creates a word array with 3 elements all of which are 100
	
	mdArray: .word 0, 1
		 .word 2, 3 # That is a multi dimensional array
	# numbers above are the same with their indexes, they are stored sequentially so can be accessed with the formula:
	# addr = baseAddr + (currentRow * columnSize + currentColumn) * dataSize.
	
	# Load syntax is the exact same	
	newline: .asciiz "\n"
	alwaysMessage: .asciiz "This message is printed always.\n"
	equalMessage: .asciiz "Numbers are equal.\n"
	loopEnd: .asciiz "\nNumber is finally: "
	
.text
	main:
		addi $t0, $zero, 10
		addi $t1, $zero, 10
	
		beq $t0, $t1, numbersEqual
		return1:
		
		# bne: not equal
		# blt: less than
		# ble: less than or equal to
		# There are many other conditionals
		
		# In order to compare float or double values, c.eq.d, c.eq.s etc. must be used.
		# The other options can be seen by writing c.
		# In order to do branching with these comparisons, bc1t, bc1f must be used
		# (Stands for branch if coprocessor1 is true-false)
		
		b always
		return2:
								
		# slt, sgt, seq might be also useful
		# assigns a register to 0 or 1 according to the condidition and numbers
		
		addi $t2, $zero, 5
		
		while:
			bge $t2, 10, exit
			
			li $v0, 1
			add $a0, $t2, $zero
			syscall
			
			addi $t2, $t2, 1
			j while
		exit:
			li $v0, 4
			la $a0, loopEnd
			syscall
			
			li $v0, 1
			add $a0, $t2, $zero
			syscall
			
			jal printNewline
			
		addi $s0, $zero, 10
		addi $s1, $zero, 20
		addi $s2, $zero, 30
			
		addi $t0, $zero, 0
		
		sw $s0, array($t0)
		addi $t0, $t0, 4
		
		sw $s1, array($t0)
		addi $t0, $t0, 4
		
		sw $s2, array($t0)

		addi $s0, $zero, 0
		addi $s1, $zero, 0
		addi $s2, $zero, 0
		
		while0:
			blt $t0, $zero, exit0
			li $v0, 1
			lw $a0, array($t0)
			syscall
			jal printNewline
			addi $t0, $t0, -4
			j while0
		exit0:
			
			
		
		li $v0, 10
		syscall
		
	numbersEqual:
		li $v0, 4
		la $a0, equalMessage
		syscall
		j return1
		
	always:
		li $v0, 4
		la $a0, alwaysMessage
		syscall
		j return2
		
	printNewline:
		li $v0, 4
		la $a0, newline
		syscall
		jr $ra
		
	# If you enter . there are some fancy features like include and global