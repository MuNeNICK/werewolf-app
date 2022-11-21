export async function getServerSideProps() {
  const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}`);
  const data = await response.json();

  return { props: { data } };
}

export default function Home( {data} ) {
  return (
    <div>
      <p>{data.content}</p>
    </div>
  )
}
