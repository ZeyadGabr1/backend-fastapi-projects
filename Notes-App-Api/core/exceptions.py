from fastapi import HTTPException, status

class NotesError(HTTPException):
    """ Base exception """
    pass


class UserError(HTTPException):
    """ Base exception """
    pass


class SystemError(HTTPException):
    """ Base exception """
    pass




class ShortTitle(NotesError):

    def __init__(self):
        message = "Title must be at least 5 characters"
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)



class LongTitle(NotesError):

    def __init__(self):
        message = "Title is too long please enter at maximum 55 characters"
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)


class ShortContent(NotesError):

    def __init__(self):
        message = "Content must be at least 15 characters"
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)



class LongContent(NotesError):

    def __init__(self):
        message = "Content is too long please enter at maximum 255 characters"
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)



class NoteIdNotFound(NotesError):

    def __init__(self, id: int):
        message = f"No note with id: {id}, please try again"
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=message)



class UserNotFound(UserError):

    def __init__(self):
        message = f"User not register please signup first"
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=message)


class IncorrectPassword(UserError):

    def __init__(self):
        message = f"Password is not correct please try again"
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)



class ShortUsername(UserError):

    def __init__(self):
        message = "Username must be at least 5 characters"
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)


class LongUsername(UserError):

    def __init__(self):
        message = "Username is too long please enter at maximum 55 characters"
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)




class ShortPassword(UserError):

    def __init__(self):
        message = "Password must be at least 8 characters"
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)


class LongPassord(UserError):

    def __init__(self):
        message = "Password is too long please enter at maximum 55 characters"
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)



class UserRegistered(UserError):

    def __init__(self):
        message = "The user is already registered, Please try to login"
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)


class InternalError(SystemError):

    def __init__(self):
        message = "An error occurred while executing the transaction. Please try again later."
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message)


class UnauthorizedUser(UserError):

    def __init__(self):
        message = "Unauthorized user please login first."
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=message)



