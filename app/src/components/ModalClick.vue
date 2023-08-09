<template>
  <div class="modal-overlay" @click="$emit('close-modal')">
    <div class="modal" @click.stop>
      <h6>Datos para la reserva</h6>
        <div class="formulary">

          <input
          id="pet_name"
          class="form_input"
          placeholder="Nombre de la mascota"
          />


          <label for="lang">¿Es de raza?</label>
          <select ref="breed" name="raza" id="lang">
          <option value="opt">Selecciona una opcion</option>
          <option value="yes">Si</option>
          <option value="no">No</option>
          </select>
          <br>
          <input
          id="pet_breed"
          class="form_input"
          placeholder="En caso afirmativo, indique qué raza"
          />
          <br>

          <input
          id="telephone"
          class="form_input"
          placeholder="Teléfono"
          />
          <br>

          <label for="lang">Edad</label>
          <select ref="age" name="edad" id="lang">
          <option value="opt">Selecciona una opcion</option>
          <option value="joven">Joven -10</option>
          <option value="senior">Senior +10</option>
          </select>
          <br><br>
          
          <label>Selecciona si existe alguna observación:</label>
          <div class="div_observations">
            <input class="div_observations" type="checkbox" id="cbox1" value="Otitis" v-model="observations"/>
            <label class="div_observations" for="otitis">Otitis</label>
          <br>
            <input class="div_observations" type="checkbox" id="cbox2" value="Artrosis" v-model="observations"/>
            <label class="div_observations" for="artrosis">Artrosis</label>
          <br>
            <input class="div_observations" type="checkbox" id="cbox3" value="Alergias" v-model="observations"/>
            <label class="div_observations" for="alergias">Alergias</label>
          <br>
            <input class="div_observations" type="checkbox" id="cbox4" value="Mordedor" v-model="observations"/>
            <label class="div_observations" for="mordedor">Mordedor</label>
          <br>

          </div>


      </div>
      <button v-on:click="save_data()">Reservar</button>
    </div>
    <div class="close" @click="$emit('close-modal')">
    </div>
  </div>
</template>

  
  <script>
    export default {
      data() {
        return {
          observations: []
      }},
  
    methods: {
      save_data() {
        console.log(this.data)

        const pet_name = document.getElementById("pet_name").value
        console.log(pet_name)

        var breed_bool = false
        this.breed = this.$refs.breed.value;
        console.log(breed_bool)
        
        const pet_breed = document.getElementById("pet_breed").value

        const telephone = document.getElementById("telephone").value
        console.log(telephone)

        var age_bool = false
        this.age = this.$refs.age.value;
        if (this.age == "yes"){
          age_bool = true}
        else{
          age_bool = false}
        console.log(age_bool)

        const booking = {
            name: pet_name,
            breed: pet_breed,
            telephone: telephone,
            age: age_bool,
            observations: this.observations
        }
        console.log(booking)
      }
  }

  }
  </script>

<style scoped>


body {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
    height: 100vh; 
    background-color: #f1f1f1;
   }

input {
    font-size: 20px;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
   }

label {
    font-family: 'Open Sans Condensed', sans-serif;
    font-size: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
   }

select {
    font-family: 'Open Sans Condensed', sans-serif;
    font-size: 17px;
    margin-bottom: 10px;
    margin-top: 10px;
   }

.form_input {
  font-family: 'Open Sans Condensed', sans-serif;
  background-color: #ffffff;
  width: 70%;
  margin: 10px;
  align-items: center;
  justify-content: center;
  
}

.div_observations{
  font-family: 'Open Sans Condensed', sans-serif;
  font-size: 20px;
  display: inline-block;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}

.modal-overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  background-color: #000000da;
  z-index: 100000;
}

.modal {
  text-align: center;
  background-color: white;
  height: 500px;
  width: 500px;
  margin-top: 10%;
  padding: 60px 0;
  border-radius: 20px;
  z-index: 100000;
}
.close {
  margin: 10% 0 0 16px;
  cursor: pointer;
}

.close-img {
  width: 25px;
}

.check {
  width: 150px;
}

h6 {
  font-weight: 500;
  font-size: 28px;
  margin: 20px 0;
}

p {
  font-size: 16px;
  margin: 20px 0;
}

button {
  background-color: #ac003e;
  width: 150px;
  height: 40px;
  color: white;
  font-size: 14px;
  border-radius: 16px;
  margin-top: 50px;
}
</style>