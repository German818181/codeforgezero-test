export async function getActiveUsers(userIds) {
  const users = [];
  
  for (const id of userIds) {
    const { data } = await supabase
      .from('profiles')
      .select('name, email')
      .eq('id', id)
      .single();
      
    if (data) users.push(data);
  }
  
  return users;
}
