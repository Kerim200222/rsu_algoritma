import time

class LinearCongruentialGenerator:
    def __init__(self, seed=None):
        # Algoritmanın temel değişkenlerini ayarlama
        # m: Modulus (Modül)
        # a: Multiplier (Çarpan)
        # c: Increment (Artış)
        self.m = 2**32
        self.a = 1664525
        self.c = 1013904223
        
        # Eğer Seed belirtilmediyse, her çalıştırmada rastgeleliği sağlamak için mevcut zamanı kullanıyoruz
        if seed is None:
            self.seed = int(time.time())
        else:
            self.seed = seed
            
        self.state = self.seed

    def random(self):
        """0 ile 1 arasında rastgele bir sayı üretir"""
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m

    def randint(self, low, high):
        """Belirli bir aralıkta rastgele bir tam sayı üretir"""
        return int(self.random() * (high - low) + low)

# --- Kodu Test Etme ---
if __name__ == "__main__":
    lcg = LinearCongruentialGenerator()
    
    print("--- Rastgele Sayı Üreteci (LCG) Testi ---")
    print(f"Seed kullanılan: {lcg.seed}")
    print("Üretilen 5 rastgele sayı:")
    
    for i in range(5):
        print(f"{i+1}. Sayı: {lcg.randint(0, 100)}") # 0 ile 100 arasında sayılar üretir