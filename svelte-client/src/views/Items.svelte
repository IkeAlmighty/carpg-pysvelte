<script>
  import { onMount } from "svelte";
  import axios from "axios";

  const API_URI = "http://localhost:5000/api";

  let items = [];

  onMount(async () => {
    axios.get(`${API_URI}/items`).then((res) => {
      items = res.data;
      console.log(items);
    });
  });
</script>

<div>
  Items:
  <div class="d-block">
    <ul class="itemframe">
      {#each items as item}
        <li>
          <strong>{item[0]}</strong>
          <div class="d-block text-small">
            Description: {item[1]}
          </div>
          <div class="d-block text-small">
            {item[2]} lbs
          </div>
          <div class="d-block text-small">
            <strong>Spell:</strong> {item[3][0]}
          </div>
        </li>
      {/each}
    </ul>
  </div>
</div>

<style>

  .itemframe {
    width: 250px;
    text-justify:distribute;
  }

  .d-block {
    display: block;
  }

  .text-small {
    font-size: smaller;
  }
</style>
