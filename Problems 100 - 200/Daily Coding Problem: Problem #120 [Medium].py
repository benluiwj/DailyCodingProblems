# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Implement the singleton pattern with a twist. First, instead of storing one
# instance, store two instances. And in every even call of getInstance(), return
# the first instance and in every odd call of getInstance(), return the second
# instance.


"""
public final class Singleton {
    private static Singleton[] instance = {null, null};
    public String value;
    private static Integer count = 0;

    private Singleton(String value) {
        this.value = value;
    }

    public static Singleton getInstance(String value) {
        if (instance[count % 2] == null) {
		instance[count % 2] = new Singleton(value);
		count++;
	}
	Singleton toReturn = instance[count % 2];
	count++;
        return toReturn;
    }
}




"""