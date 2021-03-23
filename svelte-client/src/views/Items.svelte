<script>
  import { onMount } from "svelte";
  import axios from "axios";

  const API_URI = "http://localhost:5000/api";

  let items = [];

  onMount(async () => {
    axios.get(`${API_URI}/items`).then((res) => {
      items = res.data;
      console.log(items)
    });
  });
</script>

<div>
  Items:
  <div class="d-block">
    <ul>
      {#each items as item}
        <li>
          {item[0]}
          <div class="d-block text-small">
            {item[1]}
          </div>
          <div class="d-block text-small">
            {item[2]} lbs
          </div>
        </li>
      {/each}
    </ul>
  </div>
</div>