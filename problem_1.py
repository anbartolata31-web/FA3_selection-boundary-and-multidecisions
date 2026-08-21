START
    LOOP
        PROMPT "Enter your password: "
        READ password
        SET length = LENGTH(password)
        
        IF length >= 8 AND length <= 15 THEN
            PRINT "Password length is valid."
            EXIT LOOP
        ELSE
            PRINT "Password too short or too long. Please try again."
        ENDIF
    END LOOP
END
