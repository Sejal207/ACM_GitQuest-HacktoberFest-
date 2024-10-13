class circle{
    double radius;
   
    circle(double rad){
        radius=rad;
        
    }
    double access_rad(){
        return radius;
    };
    double modify_rad(double rad){
    
        radius=rad;
        return radius;
    }
    double area(){
        return (3.141*radius*radius);
    }
    double circumference(){
        return (2*3.141*radius);
    }
    public static void main(String[] args) {
        circle c=new circle(2);
        double accessed = c.access_rad();
        System.out.println(accessed);
        double modified=c.modify_rad(3);
        System.out.println(modified);
        double calc_area =c.area();
        System.out.println(calc_area);
        double calc_cir =c.circumference();
        System.out.println(calc_cir);
    }

}