subroutine sub2_1(a, b)
    implicit none
    double precision, intent(in) :: a
    double precision, intent(out) :: b
    b = a - 1
end subroutine sub2_1

subroutine sub2_2(a, b, c)
    implicit none
    double precision, dimension(3), intent(in) :: a
    double precision, dimension(3), intent(in) :: b
    double precision, dimension(3), intent(out) :: c
    c = a - b
end subroutine sub2_2
